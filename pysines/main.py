"""
    The main script file to launch the pysines application
"""
import sys
import argparse

def check_options(options):
    """
    Check that the options are sane and restricted to the project specs
    :param options: An `argparse.Namespace` object
    :return:
    """

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An `argparse.ArgumentParser` instance
    """
    parser = argparse.ArgumentParser('pysines', description=" add description")
    
    parser.add_argument('-f', '--file',help="")
    parser.add_argument('-n', '--num', type=int, help="")
    
    return parser

def parse_args(args):
    """
    Perform the actual argument parsing, useful for testing the parser
    :param args: The list of arguments to parse, something like `sys.argv`
    :return: An `argparse.Namespace` object
    """
    parser = create_parser()
    # runs the above funciton to create our parser object, this could have all been done here
        
    return parser.parse_args(args)  #parse_args() is a method of our parser object
                                    # happens to have the same name as our function
                                    # but they are not the same thing
    
def run(options):
    """
    Run the actual script
    :param options: An `argparse.Namespace` object
    :return:
    """
    
    from matplotlib import pyplot as plt
    import numpy as np
    import os

    # select folder to save plots in                                     \/ go back one level
    plot_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'plots'))  
    
    print options.file
    print options.num
    
    
    # Create the data set 
    print
    print "Plot 1"
    time = np.linspace(0, 6 * np.pi)
    data = 2 * np.sin(time) + 3 * np.cos(time)
    
    # Create the plot 
    for i in range(1, options.num +1):
        plt.plot(time, data*i)
        
    plt.title('A title')
    plt.xlabel('Time')
    plt.ylabel('Data')
      
    # Save the plot as an exaple
    plt.savefig(os.path.join(plot_dir, options.file))
      
              
    # Do some additional check on the options
    check_options(options)
    
    
    
    
    

    pass


if __name__ == '__main__':
    # Script has been launched

    parser = create_parser()
    #options = parse_args(sys.argv)     #skip the parser_args() function and just do it below
                                        # dont explicity reference the comand line 
                                        #input sys.argv, it is already the default
    options = parser.parse_args()      
    run(options)