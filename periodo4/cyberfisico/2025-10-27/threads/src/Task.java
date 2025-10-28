

public class Task implements Runnable {

    private static final int TASK_WAIT_TIME_MS = 10;

    @Override
    public void run() {
        double result = 0;
        for (int i = 0; i < 100000; i++) {
            result += Math.sin(i) * Math.cos(i);
        }
    }

}

