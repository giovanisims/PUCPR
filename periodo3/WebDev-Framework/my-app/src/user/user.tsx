import React from "react";

interface UserModel {
    name: string;
    age?: number;
    birthdate?: any;
}

const user : React.FC<UserModel> = ({name, age}) => {
    return (
<div className="container">
Meu primeiro componente react

{name}
{age}
</div>
  )
}
export default user