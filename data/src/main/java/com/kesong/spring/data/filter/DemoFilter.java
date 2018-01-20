package com.kesong.spring.data.filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

/**
 * Created by fusu on 2018/1/16.
 */
@WebFilter(urlPatterns = {"/demo"})
public class DemoFilter implements Filter {
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("demo filter init...");
    }

    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("filter: do filter ");
    }

    public void destroy() {

    }
}
