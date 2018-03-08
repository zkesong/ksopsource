package com.kesong.spring.data.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.ContextLoader;
import org.springframework.web.context.WebApplicationContext;

import javax.servlet.http.HttpServletRequest;

/**
 * Created by fusu on 2018/1/5.
 */
@RestController
@RequestMapping("test")
public class TestController {RedisConnection

    @Autowired
    private StringRedisTemplate redisTemplate;

    @GetMapping("get")
    public void sayHello(HttpServletRequest request) {
        WebApplicationContext context = ContextLoader.getCurrentWebApplicationContext();
        LettuceConnectionFactory factory = context.getBean("lettuceConnectionFactory", LettuceConnectionFactory.class);
        System.out.println(factory);
        System.out.println(redisTemplate);
        System.out.println(redisTemplate.opsForValue().get("aa"));
    }

    @PostMapping("put")
    public void saveKeyValue(String name, String age) {
        System.out.println(name + " " + age);
        redisTemplate.opsForValue().append(name, age);
    }

    @GetMapping("gp")
    public void saveKeyValueGet(String name, String age) {
        System.out.println(name + " " + age);
        redisTemplate.opsForValue().append(name, age);
    }
}
