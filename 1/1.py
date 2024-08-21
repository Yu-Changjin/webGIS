<div id="map-div" style="width:800px;height:500px;"></div>

//引入需要的东西
import View from 'ol/View'
import Map from 'ol/Map'
import TileLayer from 'ol/layer/Tile'
import {OSM} from 'ol/source';

//显示地图的方法
showMap() {
    var map = new Map({
        layers: [
            new TileLayer({ source: new OSM() }),// 创建一个使用Open Street Map地图源的瓦片图层
        ],
        // 设置显示地图的视图
        view: new View({
          center: [0,0], // 定义地图显示中心
          zoom: 2, 
        }),
        target: "map-div", //存放地图的容器
    });
},
