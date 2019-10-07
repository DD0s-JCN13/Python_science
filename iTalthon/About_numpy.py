import numpy as np
import pandas as pd
tester_np = np.array([1, "Hello", False])
print(tester_np)
print(tester_np.dtype)
tester_pd = pd.DataFrame([[1, 18],
                         [29, 43, 55]])
print(tester_pd)

serial_num = ["nac149ac", "nac149xc", "mes177hc", "mes177hxc"]
graphic_card = ["NVMX130", "NVMX150", "NVGTX1070", "NVGTX1080"]
actual_effect = ["NB", "NB", "BES", "AES"]
price = [18900, 21950, 37990, 45900]

laptop_pd = {"Serials": serial_num,
             "Graphic Cards": graphic_card,
             "Performance": actual_effect,
             "Price(with tax)": price}
print(pd.DataFrame(laptop_pd))
"""
今天，我們就針對原本的存放方式進行優化，讓程式的輸出格式更有表格的樣子，那就先提兩個Python的模組：```numpy 與 pandas```，
只不過這兩個模組都必須要額外安裝才能使用 ~~(而我因為是用PyCharm by JetBrain，就可以透過系統內建的下載輔助來把這兩個套件直接導入到原系統)~~
在直接將這兩個方法直接套用到現有的程式之前，畢竟它是模組，所以就會需要先做導入：
```python
import numpy
import pandas
#其實可以在後面分別加上 "as np/ as pd" 這類的方式來讓接下來的操作更加輕鬆
```
```numpy```其實可以解釋為```可運算的Dictionary資料架構```，只不過這種資料架構並沒有辦法同時存放不同類型的參數，若有這種情況的時候就會變成是下面的情況：
```python
import numpy as np
tester_np = np.array([1, "Hello", False])
print(tester_np)
print(tester_np.dtype) #輸出np.array的物件屬性

輸出結果如下：
['1' 'Hello' 'False'] >>>雖然看起來並沒有不一樣
<U11 >>>但是屬性已經是以Unicode 11的結構進行存放，簡單來說，所有Array內的元素都已經轉為字串

```
"""