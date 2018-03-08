package cn.kszeng.util;

/**
 * @author Bryan Sun
 * @version V1.0
 * @e-mail bryansun@163.com
 * @date 2017/10/24 21:25
 * @Description:
 */
public class TimeUtil {
    private TimeUtil(){
    }

    public static int dayToSeconds(int day){
        return day * 24 * 60 * 60;
    }

    public static int hourToSeconds(int hour){
        return hour * 60 * 60;
    }

    public static int minuteToSeconds(int minute){
        return minute * 60;
    }
}
