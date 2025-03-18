## IndParam

```python
class IndParam:
    """
    技术指标
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: IndicatorImp) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Indicator) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def get(self) -> Indicator:
        ...
    def get_imp(self) -> IndicatorImp:
        ...
```

## 相关方法

#### AMA

```python
def AMA(n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(m: IndParam, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(m: IndParam, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: IndParam, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: IndParam, n: IndParam) -> Indicator:
    ...
```

#### MACD

```python
def MACD(n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
```

#### MACD

```python
def MACD(data: Indicator, n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(n: IndParam, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(n: IndParam, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: IndParam, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: IndParam, m: IndParam) -> Indicator:
    ...
```

