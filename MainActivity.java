package com.example.shifalishetty.cfgtrial3;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {
    public WebView mywebview;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mywebview=(WebView)findViewById(R.id.webview);
        WebSettings webSettings=mywebview.getSettings();
        webSettings.setJavaScriptEnabled(true);
        mywebview.loadUrl("http://www.xyz.com");
        mywebview.setWebViewClient(new WebViewClient());
    }

    @Override
    public void onBackPressed() {
        if(mywebview.canGoBack()) {
            mywebview.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
