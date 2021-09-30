import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  items = ["Angular", "React", "Underscore"];

  newItem: string = "";

  pushItem(){
  	if (this.newItem != "") {
  		this.items.push(this.newItem);
		  this.newItem = "";
  	}
  }

  removeItem(i){
  	this.items.splice(i, 1);
  }
}
