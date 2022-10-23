
pragma solidity ^0.6.0;



contract Token {

	struct TaxiDataStruct {
		address taxi_address;
		uint id;
		uint x;
		uint y;
		uint base_price;
		uint price_min;
		bool available;
		bool _isAlive;
	}

	mapping(address => uint) taxiAddressIds;
	mapping(uint => TaxiDataStruct) taxiIdData;
	event Available(uint taxiid, uint x, uint y, uint base_price, uint price_min);
	event Paired(address passengerAddress, uint taxiid);
	event StartJourney(address passengerAddress, uint taxiid);
	event EndJourney(address passengerAddress, uint taxiid);
	event TaxiId(uint taxiid);

	uint current_taxi_id;
	uint taxi_num;
	uint available_num;

	constructor() public {
		current_taxi_id = 0;
		taxi_num = 0;
	}



	function check_taxi_exists(uint taxiid) public{
		if (taxiIdData[taxiid]._isAlive) {
			// 'i know its deleted lol but not gonna do anything about it'
		}
	}

	function add_taxi(uint x, uint y, uint base_price, uint price_min) public {
		taxiAddressIds[msg.sender] = current_taxi_id;
		TaxiDataStruct memory newdata;
		newdata.taxi_address = msg.sender;
		newdata.id = current_taxi_id;
		newdata.x = x;
		newdata.y = y;
		newdata.base_price = base_price;
		newdata.price_min = price_min;
		newdata.available = true;
		newdata._isAlive = true;
		taxiIdData[current_taxi_id] = newdata;
		current_taxi_id += 1;
		taxi_num += 1;
		available_num +=1;

		//emit TaxiId(taxiAddressIds[msg.sender]);
		//emit Available(taxiAddressIds[msg.sender],x,y,base_price,price_min);
	}

	function pair(uint taxiid) public {
		check_taxi_exists(taxiid);
		if (taxiIdData[taxiid].available) {
			taxiIdData[taxiid].available = false;
			emit Paired(msg.sender,taxiid);
		}
		available_num -=1;
	}

	function passenger_update_taxi_location(uint taxiid, uint x, uint y) public {
		check_taxi_exists(taxiid);
		taxiIdData[taxiid].x = x;
		taxiIdData[taxiid].y = y;
	}


	function check_available_taxi_addresses(uint i) public view returns (address) {
		address address_output;


		if (taxiIdData[i]._isAlive){
			if (taxiIdData[i].available) {
				address_output=taxiIdData[i].taxi_address;

			}
		}

		return address_output;
	}

	function check_available_taxi_x(uint i) public view returns (uint) {
		uint integer_output;

		if (taxiIdData[i]._isAlive){
			if (taxiIdData[i].available) {
				integer_output = taxiIdData[i].x;
			}
		}
		return integer_output;
	}

	function check_available_taxi_y(uint i) public view returns (uint) {
		uint integer_output;

		if (taxiIdData[i]._isAlive){
			if (taxiIdData[i].available) {
				integer_output = taxiIdData[i].y;
			}
		}
		return integer_output;
	}
	function check_available_taxi_price_min(uint i) public view returns (uint) {
		uint integer_output;

		if (taxiIdData[i]._isAlive){
			if (taxiIdData[i].available) {
				integer_output = taxiIdData[i].price_min;
			}
		}
		return integer_output;
	}
	function check_available_taxi_base_price(uint i) public view returns (uint) {
		uint integer_output;

		if (taxiIdData[i]._isAlive){
			if (taxiIdData[i].available) {
				integer_output = taxiIdData[i].base_price;
			}
		}
		return integer_output;
	}


//	function check_available_taxi_ints(uint i, string memory wanted_variable) public view returns (uint) {
//		uint integer_output;
//		if (taxiIdData[i]._isAlive){
//			if (taxiIdData[i].available) {
//				if (wanted_variable == 'x'){
//					integer_output = taxiIdData[i].x;
//
//				}
//				else if (wanted_variable == 'y'){
//					integer_output = taxiIdData[i].y;
//				}
//				else if (wanted_variable == 'base_price'){
//					integer_output = taxiIdData[i].base_price;
//				}
//				else if (wanted_variable == 'y'){
//					integer_output = taxiIdData[i].price_min;
//				}
//			}
//		}
//
	//	return integer_output;
	//}

//	function check_available_taxi_booleans(uint i, string memory wanted_variable) public view returns (bool) {
//		bool boolean_output;
//
//		if (taxiIdData[i]._isAlive){
//			if (taxiIdData[i].available) {
//				if (wanted_variable == 'available'){
//					boolean_output = taxiIdData[i].available;
//				}
//				else if (wanted_variable == 'isAlive'){
//					boolean_output = taxiIdData._isAlive;
//				}
//			}
//		}
//
//		return boolean_output;
//	}


	function check_number_taxis() public view returns (uint) {
		return taxi_num;
	}

	function check_number_available() public view returns (uint) {
		return available_num;
	}

	function taxi_owner_update_details(uint base_price, uint price_min) public {
		// check_taxi_exists(taxiIdData[taxiAddressIds[msg.sender]]);
		taxiIdData[taxiAddressIds[msg.sender]].base_price = base_price;
		taxiIdData[taxiAddressIds[msg.sender]].price_min = price_min;
	}

	function taxi_received_payement(address passengerAddress) public {
		check_taxi_exists(taxiAddressIds[msg.sender]);
		emit StartJourney(passengerAddress,taxiAddressIds[msg.sender]);
	}

	function passenger_exit_taxi(uint taxiid, uint x, uint y) public {
		check_taxi_exists(taxiid);
		passenger_update_taxi_location(taxiid,x,y);
		taxiIdData[taxiid].available = true;
		emit EndJourney(msg.sender,taxiid);
		emit Available(
			taxiid,
			taxiIdData[taxiid].x,
			taxiIdData[taxiid].y,
			taxiIdData[taxiid].base_price,
			taxiIdData[taxiid].price_min
		);
	}

	function remove_taxi() public {
		uint taxi_id_to_remove = taxiAddressIds[msg.sender];
		check_taxi_exists(taxi_id_to_remove);
		taxiIdData[taxi_id_to_remove]._isAlive = true;
		taxi_num -= 1;
		delete taxiAddressIds[msg.sender];
	}


	// /**
	// 	@notice Approve an address to spend the specified amount of tokens on behalf of msg.sender
	// 	@dev Beware that changing an allowance with this method brings the risk that someone may use both the old
	// 		 and the new allowance by unfortunate transaction ordering. One possible solution to mitigate this
	// 		 race condition is to first reduce the spender's allowance to 0 and set the desired value afterwards:
	// 		 https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
	// 	@param _spender The address which will spend the funds.
	// 	@param _value The amount of tokens to be spent.
	// 	@return Success boolean
	//  */
	// function approve(address _spender, uint256 _value) public returns (bool) {
	// 	allowed[msg.sender][_spender] = _value;
	// 	emit Approval(msg.sender, _spender, _value);
	// 	return true;
	// }

	// /** shared logic for transfer and transferFrom */
	// function _transfer(address _from, address _to, uint256 _value) internal {
	// 	require(balances[_from] >= _value, "Insufficient balance");
	// 	balances[_from] = balances[_from].sub(_value);
	// 	balances[_to] = balances[_to].add(_value);
	// 	emit Transfer(_from, _to, _value);
	// }

	// /**
	// 	@notice Transfer tokens to a specified address
	// 	@param _to The address to transfer to
	// 	@param _value The amount to be transferred
	// 	@return Success boolean
	//  */
	// function transfer(address _to, uint256 _value) public returns (bool) {
	// 	_transfer(msg.sender, _to, _value);
	// 	return true;
	// }

	// /**
	// 	@notice Transfer tokens from one address to another
	// 	@param _from The address which you want to send tokens from
	// 	@param _to The address which you want to transfer to
	// 	@param _value The amount of tokens to be transferred
	// 	@return Success boolean
	//  */
	// function transferFrom(
	// 	address _from,
	// 	address _to,
	// 	uint256 _value
	// )
	// 	public
	// 	returns (bool)
	// {
	// 	require(allowed[_from][msg.sender] >= _value, "Insufficient allowance");
	// 	allowed[_from][msg.sender] = allowed[_from][msg.sender].sub(_value);
	// 	_transfer(_from, _to, _value);
	// 	return true;
	// }

}
