import java.io.File; 
import java.io.IOException; 
import java.awt.image.BufferedImage; 
import javax.imageio.ImageIO; 

public class Mario {

	public static void main(String[] args) {
		
		//space in RAM
		BufferedImage image = null;
		
		//first let's read the image
		try {
			File inFile = new File("mario.jpeg"); //! use the right directory
			//Create an image object
			image = new BufferedImage(100,100, BufferedImage.TYPE_INT_ARGB);  //the first 2 parameters represent the width and height respectively
			//reading the file
			image = ImageIO.read(inFile);
		}
		catch(IOException e) {
			//print an error message if it can not open the image
			System.out.println("ERROR " +e);
		}
		
		//Now let's display the image (using a try and catch)
		try {
			File outFile = new File ("/Users/y.g/eclipse-workspace/Mario Brothers/src/out.jpeg");
			ImageIO.write(image,"jpeg",outFile);
		}
		catch(IOException e) {
			//print an error message if it can not write the image
			System.out.println("ERROR " +e);
		}
	}

}
