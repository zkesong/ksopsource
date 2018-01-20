package com.kesong.spring.json.core;

/**
 * Created by fusu on 2018/1/15.
 */
public class CmpTask implements Runnable{

    private CmpWork work;

    public CmpTask(String name, CmpWork work) {
        this.work = work;
    }

    public void run() {

    }
}
