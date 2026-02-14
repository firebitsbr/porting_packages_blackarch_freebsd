PORTNAME=	gpp-decrypt
DISTVERSION=	v1.1.r2.g801b9d5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Parse the Group Policy Preferences XML file which extracts the username and decrypts the cpassword attribute.
WWW=		https://github.com/t0thkr1s/gpp-decrypt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-crypto@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
