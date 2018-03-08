package cn.kszeng.redis;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/29 11:03
 * @Description:
 */
public class RedisListener {
    private List<String> keys;

    public RedisListener(){
        keys = new ArrayList<>();
    }

    public RedisListener(int keyNumber){
        keys = new ArrayList<>(keyNumber);
    }

    public void listen(String key){
        keys.add(key);
    }

    public void listen(String[] keys){
        this.keys.addAll(Arrays.asList(keys));
    }

    public String[] getListeningKeys(){
        String[] keysArr = new String[keys.size()];
        return keys.toArray(keysArr);
    }
}
