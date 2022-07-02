import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reset',
  templateUrl: './reset.component.html',
  styleUrls: ['./reset.component.scss']
})
export class ResetComponent implements OnInit {

  showPassword:boolean;
  password:string;
  showPasswordConfirm:boolean;
  passwordConfirm:string;
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
