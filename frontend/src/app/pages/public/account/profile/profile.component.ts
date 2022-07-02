import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  selectedOption = 0;
  actions = [{ id: 0, name: 'Select Country' },
    { id: 1, name: 'Netherland' },
    { id: 2, name: 'England' },
    { id: 3, name: 'Scotland' },
    { id: 4, name: 'Germany' },
    { id: 5, name: 'Canada' },
    { id: 6, name: 'Mexico' },
    { id: 7, name: 'Spain' }]

  constructor() { }

  ngOnInit(): void {
  }



}
