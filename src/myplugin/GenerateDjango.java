package myplugin;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * Created by ftn
 */
public class GenerateDjango {

    public static void generateDjango(String dslLocation, String dslFileName, String outputLocation) {
        try {

            ProcessBuilder pb = null;
            if(System.getProperty("os.name").contains("Mac") || System.getProperty("os.name").contains("Linux")) {
                pb = new ProcessBuilder("python3", "generateDjangoUnix.py", dslLocation, dslFileName, outputLocation);

            }else if (System.getProperty("os.name").contains("Windows")) {
                pb = new ProcessBuilder("python3", "generateDjangoWindows.py", dslLocation, dslFileName, outputLocation);
            }

            Process p = pb.start();
            Scanner stdin = new Scanner(new InputStreamReader(p.getInputStream()));

            while (stdin.hasNext()) {
                String line = stdin.nextLine();
                System.out.println(line);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
