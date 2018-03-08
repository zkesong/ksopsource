package cn.kszeng.redis;

import redis.clients.jedis.Transaction;

import java.util.List;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/29 10:53
 * @Description:
 */
public class Executor {
    private Transaction transaction;
    public Executor(Transaction transaction){
        this.transaction = transaction;
    }

    public List<Object> execute(){
        return transaction.exec();
    }
}
