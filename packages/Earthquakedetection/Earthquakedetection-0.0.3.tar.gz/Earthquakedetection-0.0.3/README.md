
# Earthquake-detection
>This package will detect the latest earthquakes from **BMKG** *(Meteorology, Climatology, and Geophysical Agency)*.<br>
>You can use it to find out the latest earthquake news.

[![map-of-indonesia.png](https://i.postimg.cc/QNFYhPVJ/map-of-indonesia.png)](https://postimg.cc/14ZrKvG8)

### How it work
- This package will retrieve data from [BMKG](https://bmkg.go.id) to get the latest earthquake news in Indonesia.
- This package uses Beautifulsoup4 and requests.
- and will produce an output in the form of JSON that is ready to be used in web or mobile applications.

### How to use
~~~
import gempaterkini

if __name__ == '__main__':
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
~~~

### Author
wahyukmr