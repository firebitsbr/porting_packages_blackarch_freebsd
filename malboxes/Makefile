PORTNAME=	malboxes
DISTVERSION=	449.f9f310e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Builds malware analysis Windows VMs so that you dont have to.
WWW=		https://github.com/GoSecure/malboxes

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/packer \
		??/py-jinja@${PY_FLAVOR} \
		??/py-jsmin@${PY_FLAVOR} \
		??/vagrant \
		??/virtualbox \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
