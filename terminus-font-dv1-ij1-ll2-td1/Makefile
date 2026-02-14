PORTNAME=	terminus-font-dv1-ij1-ll2-td1
DISTVERSION=	4.49.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Monospace bitmap font (for X11 and console) with dv1 (cyrillic de & ve), ij1 (cyrillic i), ll2 (pass the il1I test) and td1 patches (centered ascii tilde)
WWW=		https://sourceforge.net/projects/terminus-font/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/fontconfig \
		??/python3 \
		??/xorg-bdftopcf \
		??/xorg-mkfontdir \
		??/xorg-mkfontscale

RUN_DEPENDS=	??/fontconfig \
		??/xorg-font-utils \
		??/xorg-fonts-encodings


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
