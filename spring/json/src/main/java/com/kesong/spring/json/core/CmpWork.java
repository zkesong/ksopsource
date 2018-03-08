package com.kesong.spring.json.core;

import com.kesong.spring.json.config.Setting;

/**
 * Created by fusu on 2018/1/11.
 */
public class CmpWork {
    private Job job;
    private Setting setting;

    public Job getJob() {
        return job;
    }

    public void setJob(Job job) {
        this.job = job;
    }

    public Setting getSetting() {
        return setting;
    }

    public void setSetting(Setting setting) {
        this.setting = setting;
    }

    @Override
    public String toString() {
        return "CmpWork{" +
                "job=" + job +
                ", setting=" + setting +
                '}';
    }
}
