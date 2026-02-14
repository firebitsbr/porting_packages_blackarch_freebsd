PORTNAME=	spray365
DISTVERSION=	43.22b39af
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Makes spraying Microsoft accounts (Office 365 / Azure AD) easy through its customizable two-step password spraying approach.
WWW=		https://github.com/MarkoH17/Spray365

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-click-option-group@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-msal@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
