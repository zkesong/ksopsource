package cn.kszeng.redis;

import cn.kszeng.enums.TimeEnum;
import cn.kszeng.util.TimeUtil;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.Transaction;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/24 20:18
 * @Description:
 */
public class RedisSession {
    private static final int DEFAULT_PORT = 6379;
    private Jedis jedis;
    private Transaction transaction;

    public RedisSession() {
    }

    public RedisSession(String host) {
        jedis = new Jedis(host, DEFAULT_PORT);
    }

    public RedisSession(String host, String password) {
        jedis = new Jedis(host, DEFAULT_PORT);
        authorization(password);
    }

    public RedisSession(String host, int port, String password) {
        jedis = new Jedis(host, port);
        authorization(password);
    }

    private void authorization(String password) {
        jedis.auth(password);
    }

    /**
     * set expire time for data
     *
     * @param key
     * @param time
     * @param timeEnum
     */
    public void setDataExpire(String key, int time, TimeEnum timeEnum) {
        int seconds = 0;
        switch (timeEnum) {
            case DAY:
                seconds = TimeUtil.dayToSeconds(time);
                break;
            case HOUR:
                seconds = TimeUtil.hourToSeconds(time);
                break;
            case MINUTE:
                seconds = TimeUtil.minuteToSeconds(time);
                break;
            case SECOND:
                seconds = time;
                break;
        }
        jedis.expire(key, seconds);
    }

    /**
     * get jedis
     *
     * @return the native object Jedis
     */
    public Jedis getJedis() {
        return jedis;
    }

    /**
     * transaction operation
     */
    public Executor beginTransaction() {
        transaction = jedis.multi();
        return new Executor(transaction);
    }

    public Executor beginTransaction(RedisListener listener) {
        listener = Objects.requireNonNull(listener);
        transaction.watch(listener.getListeningKeys());
        return beginTransaction();
    }

    public Transaction getTransaction() {
        return transaction;
    }

    /**
     * string operations
     */
    public String selectString(String key) {
        return selectString(0, key);
    }

    public String selectString(int dbID, String key) {
        jedis.select(dbID);
        return jedis.get(key);
    }

    public void insertString(String key, String value, boolean replacable) {
        jedis.select(0);
        if (replacable) {
            jedis.set(key, value);
            return;
        }
        jedis.setnx(key, value);
    }

    public void insertString(int dbID, String key, String value, boolean repacable) {
        jedis.select(dbID);
        insertString(key, value, repacable);
    }

    public String getAndSet(String key, String value) {
        return jedis.getSet(key, value);
    }

    public String getAndSet(int dbID, String key, String value) {
        jedis.select(dbID);
        return getAndSet(key, value);
    }

    public Long getStringLength(String key) {
        return jedis.strlen(key);
    }

    public Long getStringLength(int dbID, String key) {
        jedis.select(dbID);
        return getStringLength(key);
    }

    public void appendToString(String key, String str) {
        jedis.append(key, str);
    }

    public void appendToString(int dbID, String key, String str) {
        jedis.select(dbID);
        appendToString(key, str);
    }

    public Map<String, String> getMultiString(String... keys) {
        List<String> values = jedis.mget(keys);
        Map<String, String> map = new HashMap<>(keys.length);
        for (int i = 0; i < keys.length; i++) {
            map.put(keys[i], values.get(i));
        }
        return map;
    }

    public Map<String, String> getMultiString(int dbID, String... keys) {
        jedis.select(dbID);
        return getMultiString(keys);
    }

    /**
     * operations for hash
     */
    public void putHashMap(String key, Map<String, String> hash) {
        jedis.hmset(key, hash);
    }

    public Map<String,String> getHashMap(String key){
        return jedis.hgetAll(key);
    }

}
