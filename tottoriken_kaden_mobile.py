import folium

m = folium.Map(location=[35.3288941,133.7381978],zoom_start=10)
m

folium.Marker(location=[35.5111474,134.2013004],popup='エディオン 新鳥取本店　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[35.4774429,134.2183303],popup='エディオン 吉成店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[35.4447478,133.3297883],popup='エディオン 米子店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[35.4838863,134.2486386],popup='家電住まいる館YAMADA鳥取東店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.4778793,133.8483835],popup='ヤマダデンキ テックランド倉吉店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.518439,133.2505103],popup='ヤマダデンキ テックランド境港店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.4968155,134.2095587],popup='ヤマダデンキ テックランド鳥取店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.4377013,133.3385316],popup='ヤマダデンキ テックランドNew米子店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.5037093,133.680141],popup='ヤマダデンキ ヤマダアウトレット東伯店　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.4444928,133.3844694],popup='ケーズデンキ 日吉津店　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[35.5245846,134.2012506],popup='イオンモバイル 鳥取北店　　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[35.4457263,133.3864360],popup='イオンモバイル 日吉津店　　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[35.4675051,133.8452228],popup='100満ボルト 倉吉本店　　　　　　　　　',icon=folium.Icon(color="lightgreen")).add_to(m)
m

folium.Marker(location=[35.5131572,134.2009966],popup='パソコン工房 鳥取安長店　　　　　　　　　　　',icon=folium.Icon(color="green")).add_to(m)
m

folium.Marker(location=[35.4227735,133.3328964],popup='マーキュリー 米子　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('tottoriken_kaden_mobile.html')
