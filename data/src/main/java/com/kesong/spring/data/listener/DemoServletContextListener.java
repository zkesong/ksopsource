package com.kesong.spring.data.listener;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

/**
 * Created by fusu on 2018/1/16.
 */
@WebListener
public class DemoServletContextListener implements ServletContextListener{

    public void contextInitialized(ServletContextEvent servletContextEvent) {
        System.out.println("servlet context被初始化了....");
    }

    public void contextDestroyed(ServletContextEvent servletContextEvent) {
        System.out.println("servlet context被销毁了....");
    }
}
