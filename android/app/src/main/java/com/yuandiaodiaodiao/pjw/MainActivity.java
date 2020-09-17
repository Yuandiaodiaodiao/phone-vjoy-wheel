package com.yuandiaodiaodiao.pjw;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;

import java.util.Timer;
import java.util.concurrent.CountDownLatch;

import okio.ByteString;

public class MainActivity extends AppCompatActivity {
    long lastRepostTime=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Thread t=new Thread(()->{
            EditText tv=(EditText)findViewById(R.id.editText);
            String WS_URL="ws://" + tv.getText().toString() + ":20482/ws";
            CountDownLatch countDownLatch = new CountDownLatch(1);//创建锁
            WebSocketController.Connect(WS_URL, countDownLatch);
            try {
                countDownLatch.await();
                //这时候就已经连接完成了
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        t.start();
        SeekBar sb=(SeekBar)findViewById(R.id.seekBar);
        sb.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                long nowTime=System.currentTimeMillis();
                if(nowTime>lastRepostTime+16){
                    //保证60fps上报
                    lastRepostTime=nowTime;
                    String s=((Integer)progress).toString();
                    WebSocketController.Write(s.getBytes());
                }

            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }
}
