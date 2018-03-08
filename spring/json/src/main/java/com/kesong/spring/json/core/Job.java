package com.kesong.spring.json.core;

import java.util.Arrays;

/**
 * Created by fusu on 2018/1/8.
 */
public class Job {
    private Job.JobContent content;

    public Job.JobContent getContent() {
        return content;
    }

    public void setContent(Job.JobContent content) {
        this.content = content;
    }

    public static class JobContent {
        private String database;
        private String type;
        private String mechanism;
        private String[] sources;

        public String getDatabase() {
            return database;
        }

        public void setDatabase(String database) {
            this.database = database;
        }

        public String getType() {
            return type;
        }

        public void setType(String type) {
            this.type = type;
        }

        public String getMechanism() {
            return mechanism;
        }

        public void setMechanism(String mechanism) {
            this.mechanism = mechanism;
        }

        public String[] getSources() {
            return sources;
        }

        public void setSources(String[] sources) {
            this.sources = sources;
        }

        @Override
        public String toString() {
            return "JobContent{" +
                    "database='" + database + '\'' +
                    ", type='" + type + '\'' +
                    ", mechanism='" + mechanism + '\'' +
                    ", sources=" + Arrays.toString(sources) +
                    '}';
        }
    }

    @Override
    public String toString() {
        return "Job{" +
                "content=" + content +
                '}';
    }
}
