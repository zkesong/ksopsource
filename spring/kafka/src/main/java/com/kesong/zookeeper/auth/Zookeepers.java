package com.kesong.zookeeper.auth;

import com.kesong.zookeeper.constants.User;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.ZooKeeper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.Properties;

/**
 * Created by fusu on 2018/1/24.
 */
public class Zookeepers {

    private static String host = "localhost";

    private static int port = 8080;

    private static int timeout = 5000;

    private String authInfo;

    private static Properties zookProps = new Properties();

    private final static Logger logger = LoggerFactory.getLogger(Zookeepers.class);

    static {
        try {
            zookProps.load(Thread.currentThread().getContextClassLoader().getResourceAsStream("zookeeper.properties"));
        } catch (Exception e) {
            logger.info("zookeeper.properties配置文件不存在或者有错误");
        }
    }

    private ZooKeeper instanceZookeeper(String host, int port, int timeout, Watcher watcher, String userName, String password) {
        ZooKeeper zooKeeper = null;
        initAuthInfo(userName, password);

        String connectStr = host + ":" + port;
        try {
            zooKeeper = new ZooKeeper(connectStr, timeout, watcher);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return zooKeeper;
    }

    private void initAuthInfo(String username, String password) {
        this.authInfo = username + ":" + password;
    }

    private String getAuthInfo() {
        return this.authInfo;
    }

    private void authentication(ZooKeeper zooKeeper, String user) {
        zooKeeper.addAuthInfo(user, authInfo.getBytes());
    }

    public static ZooKeeper getClient(String user, Watcher watcher) {
        return getClient(null, 0, 0, null, null, user, watcher);
    }

    public static ZooKeeper getClient(String host,int port,int timeout,String userName, String password, String user, Watcher watcher) {
        Zookeepers zookeepers = new Zookeepers();
        ZooKeeper zooKeeper = null;
        if(zookProps.isEmpty()) {
            if(host == null)
                throw new IllegalStateException("获取zookeeper客户端连接需要配置参数或者配置文件");
            zooKeeper = zookeepers.instanceZookeeper(host, port, timeout, watcher, userName, password);
        } else {
            zooKeeper = zookeepers.instanceZookeeper(zookProps.getProperty("host"), Integer.valueOf(zookProps.getProperty("port")),
                    Integer.valueOf(zookProps.getProperty("timeout")), watcher, zookProps.getProperty("username"), zookProps.getProperty("password"));
        }
        if(User.SUPER.equals(user)) {
            zookeepers.authentication(zooKeeper, user);
        }
        return zooKeeper;
    }
}
