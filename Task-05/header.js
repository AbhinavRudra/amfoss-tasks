class Header extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
      <div class="logo"><a href="index.html"><img src="images/logo.png" width="35px" height="35px"></a>
      </div> 
      <nav>
          <ol class="links">
          
              <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q?si=Gel1D0CkRaShWhlup3Y8ww">
                  <i class="fab fa-spotify" style="color: #2bdae1;"></i>
              </a></li>
          
          
              <li><a href="https://twitter.com/imaginedragons">
                  <i class="fab fa-twitter" style="color: #2bdae1;">
              </i></a></li>
         
         
              <li><a href="https://www.youtube.com/imaginedragons"><i class="fab fa-youtube" style="color: #2bdae1;">
                  </i></a></li>
          
          
              <li><a href="https://www.instagram.com/imaginedragons/"><i class="fab fa-instagram" style="color: #2bdae1;">
                  </i></a></li>
          </ol>
      </nav>

     
      `;
    }
}

customElements.define('main-header', Header);