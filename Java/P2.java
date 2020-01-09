import javax.swing.JFrame;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
public class MoonCake {
	public static void main(String[] args) {
		JFrame frame = new JFrame();
		  ImageIcon icon = new ImageIcon("/Users/y.g/eclipse-workspace/Mario Brothers/src/mooncake.jpeg");
		  JLabel label = new JLabel(icon);
		  frame.add(label);
		  frame.setDefaultCloseOperation
		         (JFrame.EXIT_ON_CLOSE);
		  frame.pack();
		  frame.setVisible(true);

	}

}
