package myplugin;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * Created by ftn
 */
public class GenerateDjango {


    /**
     * Need to check if there more than one python installed on the system. If there is multiple python,
     * in most cases it means that Python 2.7 will have keyword "python" and Python 3.xx will have 'python3'.
     *
     * Recommended and minimum python version is: Python 3.xx.
     *
     * @param dslLocation absolute path of file which contains program code written in jsd DSL language
     * @param dslFileName name of the file which contains program code written in jsd DSL language
     * @param outputLocation absolute path of folder where will be the code generated
     */
    public static void generateDjango(String dslLocation, String dslFileName, String outputLocation) {
        try {

            ProcessBuilder pb = null;
            if(System.getProperty("os.name").contains("Mac") || System.getProperty("os.name").contains("Linux")) {
                pb = new ProcessBuilder("python", "generateDjangoUnix.py", dslLocation, dslFileName, outputLocation);

            }else if (System.getProperty("os.name").contains("Windows")) {
                pb = new ProcessBuilder("python", "generateDjangoWindows.py", dslLocation, dslFileName, outputLocation);
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
