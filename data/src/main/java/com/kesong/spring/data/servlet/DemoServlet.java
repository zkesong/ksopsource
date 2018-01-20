package com.kesong.spring.data.servlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Created by fusu on 2018/1/16.
 */
@WebServlet(urlPatterns = {"/demo"})
public class DemoServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("接收到一个请求....");
        System.out.println("url: " + req.getRequestURL());
    }
}
