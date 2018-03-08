package cn.kszeng.redis;

import cn.kszeng.io.Resource;
import cn.kszeng.util.StringUtil;
import redis.clients.jedis.Jedis;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/24 20:19
 * @Description:
 */
public class RedisSessionFactoryBuilder {
    private RedisSessionFactory factory;
    private Properties prop;

    public RedisSessionFactoryBuilder(){
    }

    public RedisSessionFactoryBuilder parseConfig(String configLocation){
        InputStream in = Resource.getResourceAsStream(configLocation);
        try {
            prop = new Properties();
            prop.load(in);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return this;
    }

    public RedisSessionFactory build(){
        factory = new RedisSessionFactory();
        factory.setHost(prop.getProperty("host"));
        if(StringUtil.hasLength(prop.getProperty("port")))
            factory.setPort(Integer.valueOf(prop.getProperty("port")).intValue());
        factory.setPassword(prop.getProperty("password"));
        return factory;
    }

    public RedisSessionFactory build(String host){
        factory = new RedisSessionFactory();
        factory.setHost(host);
        return factory;
    }

    public RedisSessionFactory build(String host,int port){
        factory = new RedisSessionFactory();
        factory.setHost(host);
        factory.setPort(port);
        return factory;
    }

    public RedisSessionFactory build(String host,String password){
        factory = new RedisSessionFactory();
        factory.setHost(host);
        factory.setPassword(password);
        return factory;
    }

    public RedisSessionFactory build(String host,int port,String password){
        factory = new RedisSessionFactory();
        factory.setHost(host);
        factory.setPassword(password);
        factory.setPort(port);
        return factory;
    }
}
