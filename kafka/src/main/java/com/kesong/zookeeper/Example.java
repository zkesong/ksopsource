package com.kesong.zookeeper;

import com.kesong.zookeeper.auth.Zookeepers;
import com.kesong.zookeeper.constants.User;
import org.apache.zookeeper.*;

import java.io.IOException;
import java.util.concurrent.CountDownLatch;

/**
 * Created by fusu on 2018/1/24.
 */
public class Example implements Watcher{
    private static CountDownLatch connectedSemaphore = new CountDownLatch(1);

    public static void main(String[] args) throws KeeperException, InterruptedException, IOException {
//        ZooKeeper zookeeper = new ZooKeeper("192.168.131.10:2181", 5000, new Example());
//        System.out.println(zookeeper.getState());
//        connectedSemaphore.await();
//        System.out.println(zookeeper.getSessionId());
//        zookeeper.addAuthInfo("digest", "master:hadoop".getBytes());
//        System.out.println(zookeeper.getChildren("/", false));
//        String path1 = zookeeper.create("/zk-test-ephemeral", "".getBytes(), ZooDefs.Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL);
//        System.out.println("Success create znode: " + path1);
//
//        String path2 = zookeeper.create("/zk-test-ephemeral-seq", "".getBytes(), ZooDefs.Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL_SEQUENTIAL);
//        System.out.println("Success create znode: " + path2);

        ZooKeeper zooKeeper = Zookeepers.getClient(User.SUPER, null);
        System.out.println(zooKeeper.getChildren("/", false));
    }


    @Override
    public void process(WatchedEvent event) {
        if (Event.KeeperState.SyncConnected == event.getState()) {
            System.out.println("CONNECTED COUNT DOWN 1");
            connectedSemaphore.countDown();
        }
    }

}
