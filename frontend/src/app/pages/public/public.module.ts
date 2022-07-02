import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PublicRoutingModule } from './public-routing.module';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from 'src/app/layouts/public-layout/header/header.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { FaqComponent } from './faq/faq.component';
import { PricingComponent } from './pricing/pricing.component';
import { BlogComponent } from './blog/blog.component';
import { PortfolioComponent } from './portfolio/portfolio.component';
import { PortfolioDetailComponent } from './portfolio-detail/portfolio-detail.component';
import { BlogDetailComponent } from './blog-detail/blog-detail.component';
import { PasswordComponent } from './account/password/password.component';
import { ProfileComponent } from './account/profile/profile.component';

@NgModule({
  declarations: [
    HomeComponent,
    HeaderComponent,
    AboutComponent,
    ContactComponent,
    FaqComponent,
    PricingComponent,
    BlogComponent,
    PortfolioComponent,
    PortfolioDetailComponent,
    BlogDetailComponent,
    PasswordComponent,
    ProfileComponent
  ],
  imports: [
    CommonModule,
    PublicRoutingModule
  ],
  exports:[
    HeaderComponent
  ]
})
export class PublicModule { }
