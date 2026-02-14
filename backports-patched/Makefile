PORTNAME=	backports-patched
DISTVERSION=	3.12.1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Backports provides drivers released on newer kernels backported for usage on older kernels. Patched flavor
WWW=		https://backports.wiki.kernel.org/index.php/Main_Page

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/linux-api-headers \
		??/linux-headers

RUN_DEPENDS=	??/linux


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
