from fastmcp import FastMCP

mcp = FastMCP("floateger-demo")

@mcp.tool
def add_floateger(a: float, b: float) -> float:
    '''
    Addition of two floategers
    
    :param a: First floateger
    :type a: float
    :param b: Second floateger
    :type b: float
    :return: Sum of a and b
    :rtype: float
    '''
    return a + b
@mcp.tool
def multiply_floateger(a: float, b: float) -> float:
    '''
    Docstring for multiply_floateger
    
    :param a: First floateger
    :type a: float
    :param b: Second floateger
    :type b: float
    :return: Multiplication of two floategers
    :rtype: float
    '''
    return a * b
@mcp.tool
def divide_floateger(a: float, b: float) -> float:
    '''
    Docstring for divide_floateger
    
    :param a: First floateger
    :type a: float
    :param b: Second floateger
    :type b: float
    :return: division of two floategers
    :rtype: float
    '''
    return a/b


if __name__ == "__main__":
    mcp.run()