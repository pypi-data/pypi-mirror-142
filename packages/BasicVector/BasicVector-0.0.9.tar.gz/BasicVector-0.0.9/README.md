# **Python basic vector**

You can find the project here : https://framagit.org/PLOTFINDER/python-basic-vector

## Vectors :

- #### Vec2 ( float, float )
    - Attributes
        - x ( get, set )
        - y (get, set)
    
    - Methods
        - div ( float, float, float )
        - mult ( float, float, float )
        - length () : returns the length of the vector
        - normalize () : normalizes the vector
        - normal() : returns a normalized vector
        - getPos() : returns the position in a form of a tuple
        - clone() : returns a clone of the Vector class
      
    - Class methods
        - dist( Vec2, Vec2) : returns the distance between two 2D vectors
        - degreesToVec2 ( float ): converts degrees to Vec2 and returns the result
        - radiansToVec2 ( float ): converts radians to Vec2 and returns the result
        - vec2ToRadians ( float ): converts vec2 to an angle in radians and returns the result 
        - vec2ToDegrees ( float ): converts vec2 to an angle in degrees and returns the result 
        - collinear ( Vec2, Vec2, Vec2 ) : looks if the 3 vectors are collinear and returns True or False 
        - between( Vec2, Vec2, Vec2 ) : looks if the target vector is between two vectors
        - lerp ( Vec2, Vec2, float ) -> Vec2

- #### Vec3 ( float, float, float )
    - Attributes
        - x ( get, set )
        - y ( get, set )
        - z ( get, set )
    
    - Methods
        - div ( float, float, float, float )
        - mult ( float, float, float, float )
        - length () : returns the length of the vector
        - normalize () : normalizes the vector 
        - normal() : returns a normalized vector
        - getPos() : returns the position in a form of a tuple
        - clone() : returns a clone of the Vector class
    
    - Class methods
        - dist( Vec3, Vec3) : returns the distance between two 3D vectors
        - collinear ( Vec3, Vec3, Vec3 ) : looks if the 3 vectors are collinear and returns True or False 
        - between( Vec3, Vec3, Vec3 ) : looks if the target vector is between two vectors
        - lerp ( Vec3, Vec3, float ) -> Vec3
    
- #### Vec4 ( float, float, float, float )
    - Attributes
        - x ( get, set )
        - y ( get, set )
        - w ( get, set )
        - h ( get, set )
    
    - Methods
        - div ( float, float, float, float, float ) -> Vec4
        - mult ( float, float, float, float, float ) -> Vec4
        - length () : returns the length of the vector
        - normalize () : normalizes the vector
        - normal() : returns a normalized vector
        - getPos() : returns the position in a form of a tuple
        - clone() : returns a clone of the Vector class
    
    - Class methods
        - dist( Vec4, Vec4) : returns the distance between two 4D vectors
        - collinear ( Vec4, Vec4, Vec4 ) : looks if the 3 vectors are collinear and returns True or False 
        - between( Vec4, Vec4, Vec4 ) : looks if the target vector is between two vectors
        - lerp ( Vec4, Vec4, float ) -> Vec4