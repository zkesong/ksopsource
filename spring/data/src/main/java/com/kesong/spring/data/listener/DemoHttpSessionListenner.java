package com.kesong.spring.data.listener;

import javax.servlet.annotation.WebListener;
import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionListener;

/**
 * Created by fusu on 2018/1/16.
 */
@WebListener
public class DemoHttpSessionListenner implements HttpSessionListener{

    public void sessionCreated(HttpSessionEvent httpSessionEvent) {
        System.out.println("http session created");
    }

    public void sessionDestroyed(HttpSessionEvent httpSessionEvent) {
        System.out.println("http session destroyed");
    }
}
