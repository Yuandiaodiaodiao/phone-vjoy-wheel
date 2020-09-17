# phone-vjoy-wheel  
websocket实现手机到vjoy的映射  

 安卓端通过okhttp3.websocket传输给tornado的websocketserver  
 通过pyvjoy库来使用vjoy的接口  
 
 python端请安装  
 pip install tornado  
 pip install vjoy  
 启动wsServer.py  
 需要>=Python3.6
 
 安卓端jdk1.8  
 依赖okhttp3.0   
 理论上拿androidstudio直接构建就行  
 最小兼容性android8  
  
