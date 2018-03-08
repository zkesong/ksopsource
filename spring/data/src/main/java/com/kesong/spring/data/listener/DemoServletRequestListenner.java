package com.kesong.spring.data.listener;

import javax.servlet.ServletRequestEvent;
import javax.servlet.ServletRequestListener;
import javax.servlet.annotation.WebListener;

/**
 * Created by fusu on 2018/1/16.
 */
@WebListener
public class DemoServletRequestListenner implements ServletRequestListener {
    public void requestDestroyed(ServletRequestEvent servletRequestEvent) {

    }

    public void requestInitialized(ServletRequestEvent servletRequestEvent) {
        System.out.println("servlet request created");
        String name = servletRequestEvent.getServletRequest().getParameter("name");
        System.out.println("请求参数：name = " + name);
    }
}
