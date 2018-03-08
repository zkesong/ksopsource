package cn.kszeng.util;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/24 20:50
 * @Description:
 */
public class StringUtil {
    private StringUtil(){
    }

    public static boolean hasLength(String str){
        return str != null && !str.equals("");
    }
}
