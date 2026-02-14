PORTNAME=	seth
DISTVERSION=	106.6e869cd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Perform a MitM attack and extract clear text credentials from RDP connections.
WWW=		https://github.com/SySS-Research/Seth

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/dsniff \
		??/tcpdump \
		lang/python \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
