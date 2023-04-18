import sys
import io
import PIL.Image as Image
import base64
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
from statsmodels.sandbox.regression.sympy_diff import df
from userInfo import user
"""
Folium in PyQt5
"""
import sqlite3
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')
        self.window_width, self.window_height = 1200, 900
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        location=(13.133932434766733, 16.103938729508073 )
        # Create the map
        self.myMap = folium.Map(
                    # tiles='Stamen Terrain',
                    zoom_start=2.5,
                    location=location
                )
        # Get the marker of the data
        self.getData()
        # save map data to data object
        data = io.BytesIO()
        self.myMap.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setContentsMargins(50,50,50,50)
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        print(user)


    def popupHtml(self,row):
        countryName=row[0]
        cityName = row[1]
        description = row[5]
        sizes = str(Image.open(io.BytesIO(row[4])))
        # print(sizes)

        img = base64.b64encode(row[4]).decode('utf-8')

        # print(img.decode('utf-8') )
        # fina = img.decode('utf-8')
        # print(img)

        html = """
            <!DOCTYPE html>
                <html>   
                    <header>

                    </header>
                    <body>
                         <h1>Country : """+countryName+"""</h1>
                        <div >
                            <img src="data:image/jpeg;base64, """+img+""" alt="logo" style="max-width:100%;height:auto;" >
                        </div>
                        
                        <h2>"""+cityName+""" City</h2>
                        <textarea rows="4" cols="50" style="border:none;font-size:15px;">"""+description+"""</textarea>
                    
                    
                    </body>       
                   
                </html>
        """

        return html


    def getData(self):
        try:
            my_dataBase = sqlite3.connect('users.db')
            curs = my_dataBase.cursor()
            query = "SELECT COUNTRY,CITY,LAT,LNG,IMG,DESCRIPTION FROM PLACES WHERE USER_ID = 1"
            curs.execute(query)

            rows = curs.fetchall()
            # print(img)


            for row in rows:
                # print(row)
                html = self.popupHtml(row)
                popup = folium.Popup(folium.Html(html, script=True), max_width=500)
                folium.Marker(

                    [row[2],row[3]],
                    popup=popup,
                    icon=folium.Icon(color='red', icon='heart', prefix='fa')
                ).add_to(self.myMap)


            curs.close()
        except sqlite3.Error as er:
            print("connection to the database failed " , er)
        finally:
            my_dataBase.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
