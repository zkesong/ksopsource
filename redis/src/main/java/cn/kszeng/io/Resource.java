package cn.kszeng.io;

import java.io.InputStream;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/29 11:19
 * @Description:
 */
public class Resource {

    private Resource(){
    }

    public static InputStream getResourceAsStream(String path){
        return Resource.class.getClassLoader()
                .getResourceAsStream(path);
    }
}
