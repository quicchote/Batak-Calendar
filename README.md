# BatakCosmogram
Approximation routine for transforming Gregorian Calendar into Indonesian traditional Batak Cosmogram. Bataknese calendar is lunar one, the new month is as the coming of the new moon that appears after the sunset every month. The new year is the evening of the new month where the constellation of Scorpio (Batak: Siala Porima) rising in the east and the constellation of Orion (Batak: Siala Sungsang) setting in the west. Thus Bataknese traditional calendar requires considering several astronomical phenomena:

1. **Lunar Month**: The Bataknese calendar is lunar, with months beginning at the sighting of the new moon. A lunar month averages about 29.53 days. By tracking the phases of the moon, we can estimate the beginning of each month with the appearance of the new moon.
2. **Constellations' Position**: The new year begins when Scorpio is rising in the east, and Orion is setting in the west at sunset. This specific alignment happens once a year, marking the start of the new year in the Bataknese calendar. This is the key event marking the new year in Bataknese Calendar/Cosmogram. This event typically occurs around late April or early May, as constellations' visibility shifts with the Earth's orbit around the Sun.
3. **Location**: Astronomical events are observed from Jakarta, Indonesia. The location's latitude and longitude affect the visibility and timing of constellations and the moon.

Since bataknese new year is based on the rising of constellation of scorpio in the east and the constellation of orion setting in the west, there will some years that have 13 month in a year, they call it **Lamadu Year**. 

The initiative demonstrated here emulate the experiental observation (rukyatulhilal) from the Lake Toba, North Sumatera, Indonesia - the origin place of the Batak people.

### Requirement Module
ephem - PyEphem

Instal: pip install ephem

Refer to the remarks within the function for detail.

### Usage

Run the code by changing the Gregorian Date you want to transform into the date and month in traditional Batak Cosmogram. 

### For more info
This is part of the work for Budaya-Indonesia.org within the Bandung Fe Institute.

Feel free to contact:
Institut Batakologi http://batakologi.id/

There's a recommended part in Chapter 1 in the book (written in Bahasa Indonesia) [**Enigma Pusaka di Kepulauan Indonesia**](https://play.google.com/store/books/details/Hokky_Situngkir_Enigma_Pusaka_di_Kepulauan_Indones?id=CxfgEAAAQBAJ) for initial understanding on conceptual Indonesian traditional cosmogram/calendar. 


