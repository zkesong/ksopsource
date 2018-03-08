package com.kesong.spring.json.test;

import com.alibaba.fastjson.JSON;
import com.kesong.spring.json.core.CmpWork;

import java.io.IOException;
import java.io.InputStream;

/**
 * Created by fusu on 2018/1/8.
 */
public class Demo2 {
    public static void main(String[] args){
        InputStream inputStream = Thread.currentThread().getContextClassLoader()
                .getResourceAsStream("compare.json");
        try {
            CmpWork work = JSON.parseObject(inputStream, CmpWork.class);
            System.out.println(work.getJob().getContent().getMechanism());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
