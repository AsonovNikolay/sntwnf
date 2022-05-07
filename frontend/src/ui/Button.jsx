import React from 'react';
import {Link} from "react-router-dom";

const Button = (props) => {
	return (
		<Link to={props.link} className={props.styles}>{props.children}</Link>
	);
};

export default Button;