import static java.lang.Thread.sleep;

public class Task implements Runnable {

    private static final int TASK_WAIT_TIME_MS = 10;

    @Override
    public void run() {
        try {
            sleep(10);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

}

