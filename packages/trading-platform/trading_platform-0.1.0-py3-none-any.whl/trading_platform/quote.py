from __future__ import annotations
from typing import List, Tuple
from enum import Enum
from datetime import datetime, timezone


class Trend(Enum):
	UP = "up"
	DOWN = "down"
	NA = "na"

class Quote:

	def __init__(self, data: dict)-> None:
		keys = ["symbol", "open", "close", "high", "low", "volume", "timestamp"]
		for key in keys:
			if key not in data:
				raise Exception(f"Data provided missing key {key}")
		self.symbol = data["symbol"]
		self.open = float(data["open"])
		self.close = float(data["close"])
		self.high = float(data["high"])
		self.low = float(data["low"])
		self.volume = int(data["volume"])
		self.timestamp = int(data["timestamp"])

		dt = datetime.fromtimestamp(self.timestamp, tz=timezone.utc)
		self.datetime = dt.strftime("%Y-%m-%d %H:%M:%S")

	def to_dict(self)-> dict:
		return {
			"symbol": self.symbol,
			"open": self.open,
			"close": self.close,
			"high": self.high,
			"low": self.low,
			"volume": self.volume,
			"timestamp": self.timestamp
		}


class QuoteCollection:

	def __init__(self, quotes: List[dict])-> None:
		self.quotes = [Quote(q) for q in quotes]

	def _sort(self):
		self.candles = sorted(self.candles, key = lambda d: d.timestamp)

	def to_dict(self)-> List[dict]:
		return [quote.to_dict() for quote in self.quotes]

	def add(self, quote: Quote)-> List[Quote]:
		self.quotes.append(quote)
		self._sort()

		return self.candles

	def get_trend(self)-> Trend:
		"""
		Returns the trend as an enum. 

		Possible outputs:

			-Tuple.UP if trend is going up
			
			-Tuple.DOWN if trend is heading down

			-Tuple.NA if trend could not be calculated
		"""
		(lows, highs, _both,) = self.get_trend_reverses()

		if len(highs) < 2 or len(lows) < 2:
			return Trend.NA

		if lows[-1].close > lows[-2].close:
			return Trend.UP
		else:
			return Trend.DOWN

	def get_trend_reverses(self)-> Tuple[List[Quote]]:
		"""
		Returns a tupple containing:

			-The lows reverse candles as a list

			-The highs reverse candles as a list

			-Both highs and lows reverse candles in chronological order as a list
		
		### Example:
		```python
		cc = CandleCollection()
		(lows, highs, both) = cc.get_trend_reverses()
		```
		"""
		direction = 0
		prev_candle = self.candles[0]
		highs = []
		lows = []
		reverses = []

		for i, candle in enumerate(self.candles):
			if i == 0:
				continue
			
			current_direction = 0
			if candle.close > prev_candle.close:
				current_direction = 1
			elif candle.close < prev_candle.close:
				current_direction = -1
			else:
				current_direction = 0

			if direction != 0 and direction != current_direction:
				# reverse point found
				if direction > current_direction:
					highs.append(prev_candle)

				if direction < current_direction:
					lows.append(prev_candle)

				reverses.append(prev_candle)

			prev_candle = candle
			direction = current_direction

		return (lows, highs, reverses,)

	def is_up_trend(self)-> bool:
		"""
		Returns boolean: 
		
			-True if the candles in the collection form an up trend

			-False if the candles form a down trend or if the trend cannot be inferred from the current candles
		
		### Example:
		```python
		cc = CandleCollection()
		if cc.is_up_trend():
			pass # do something here
		```
		"""
		return True if self.get_trend() == Trend.UP else False

	def is_down_trend(self)-> bool:
		return True if self.get_trend() == Trend.DOWN else False

	def get_support(self)-> float | None:
		"""
		Returns the support price for the current candles.
		
		Can return None if:

			-There are less than 2 low reverse point candles in the collection
			
			-The last low reverse candle breaks the past support price

		### Example:
		```python
		cc = CandleCollection()
		support = cc.get_support() # 103.55
		```
		"""
		(lows, _highs, _both,) = self.get_trend_reverses()
		if len(lows) < 2:
			return None

		support = lows[-2]
		if lows[-1].close < support.close:
			return None

		return support.close

	def get_resistance(self)-> float | None:
		"""
		Returns the resistance price for the current candles.
		
		Can return None if:

			-There are less than 2 high reverse point candles in the collection
			
			-The last high reverse candle breaks the past resistance price

		### Example:
		```python
		cc = CandleCollection()
		resistance = cc.get_resistance() # 103.55
		```
		"""
		(_lows, highs, _both,) = self.get_trend_reverses()
		if len(highs) < 2:
			return None

		resistance = highs[-2]
		if highs[-1].close > resistance.close:
			return None

		return resistance.close

	def is_impulse(self)-> bool | None:
		if len(self.candles) == 0:
			return None

		(_lows, _highs, both) = self.get_trend_reverses()
		if len(both) == 0:
			last_reverse = self.candles[0]
		else:
			last_reverse = both[-1]

		last_candle = self.candles[-1]

		if last_reverse.timestamp == last_candle.timestamp:
			return False

		if last_reverse.close > last_candle.close:
			return False

		return True
