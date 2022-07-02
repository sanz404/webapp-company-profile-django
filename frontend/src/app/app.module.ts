import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { ChartsModule } from 'ng2-charts';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PublicLayoutComponent } from './layouts/public-layout/public-layout.component';
import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { NavigationComponent } from 'src/app/layouts/public-layout/navigation/navigation.component';
import { NavigationComponent as AdminNavigationComponent } from 'src/app/layouts/admin-layout/navigation/navigation.component';
import { FooterComponent } from 'src/app/layouts/public-layout/footer/footer.component';
import { ErrorLayoutComponent } from './layouts/error-layout/error-layout.component';
import { AuthLayoutComponent } from './layouts/auth-layout/auth-layout.component';
import { NgxLoadingModule } from "ngx-loading";

import { TitleService } from './shared/services/title.service';
import { SidebarComponent } from './layouts/admin-layout/sidebar/sidebar.component';



@NgModule({
  declarations: [
    AppComponent,
    PublicLayoutComponent,
    AdminLayoutComponent,
    NavigationComponent,
    AdminNavigationComponent,
    FooterComponent,
    ErrorLayoutComponent,
    AuthLayoutComponent,
    SidebarComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    ChartsModule,
    NgxLoadingModule.forRoot({})
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(public titleService: TitleService) {}
}
