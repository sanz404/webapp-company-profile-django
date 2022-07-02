import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  showPassword:boolean;
  password:string;
  showPasswordConfirm:boolean;
  passwordConfirm:string;
  username:string;
  email:string;

  constructor() { }

  ngOnInit(): void {
  }

  toggleShow(event: any){
    this.showPassword = !this.showPassword
  }

  toggleShowConfirm(event: any){
    this.showPasswordConfirm = !this.showPasswordConfirm
  }

}
